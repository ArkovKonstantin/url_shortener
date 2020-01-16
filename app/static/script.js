function copy(str){
    let tmp = document.createElement('INPUT');
    focus = document.activeElement;
    tmp.value = str;
    document.body.appendChild(tmp);
    tmp.select();
    document.execCommand('copy');
    document.body.removeChild(tmp);
    focus.focus();
}
window.onload = function(){
    console.log('111');
    let copyBtn = document.getElementById('copy');
    let reshortBtn = document.getElementById('reshort');
    // console.log(copyBtn);
    if (copyBtn && reshortBtn){
        reshortBtn.onclick = function(e){
            console.log(location);
            window.location.replace(location.origin);
            // location;
        }
        copyBtn.onclick = function(e){
        let short_url = document.getElementById('url').placeholder;
        copy(short_url);       
        };
    };
}
