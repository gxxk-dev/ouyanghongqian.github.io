const version = 'offline-cache-v1'

self.addEventListener('install', function (event) {
    event.waitUntil(self.skipWaiting());
});

self.addEventListener('activate', function (event) {
    event.waitUntil(
        Promise.all([
            self.clients.claim(),
            caches.keys().then(function (cacheList) {
                return Promise.all(
                    cacheList.map(function (cacheName) {
                        if (cacheName !== version) {
                            return caches.delete(cacheName);
                        }
                    })
                );
            })
        ])
    );
});

self.addEventListener('fetch', function (event) {
    
    console.log('url is', event.request.url)

    event.respondWith(
        caches.match(event.request).then(function (response) {
            if (response) {
                return response;
            }

            var request = event.request.clone();
            return fetch(request).then(function (httpRes) {
                if (!httpRes || httpRes.status !== 200) {
                    return httpRes;
                }

                var responseClone = httpRes.clone();
                caches.open(version).then(function (cache) {
                    cache.put(event.request, responseClone);
                });

                return httpRes;
            });
        })
    );
})