function changeTimes() {
    var list;
    list = document.getElementsByClassName("dateTime");
    var item, index, utcTime, clientTime;
    for (index=0; index<list.length; index++){
        item = list[index];
        utcTime=item.innerHTML;
        clientTime = new Date(utcTime);
        console.log(clientTime);
        item.innerHTML = clientTime.toLocaleString();
    }
}

if (document.readyState !== 'loading') {
  changeTimes();
} else {
  document.addEventListener('DOMContentLoaded', changeTimes);
}