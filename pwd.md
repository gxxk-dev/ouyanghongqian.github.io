# str_md5生成
<script src="./md5.js"></script>
<script>
    function md5(){
        var inputvalue=document.getElementById('md5str').value
        console.log(md5(inputvalue))
    }
</script>
<input id="md5str" type="text"/><button onclick='md5()'>生成</button>
