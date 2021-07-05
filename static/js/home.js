var its = document.getElementsByClassName("item");
for (var i = 0; i < its.length; i++) {
    its[i].onclick = function () {
        // TODO: set this.className to active (ambience only)
        // TODO: remove active from all other classnames (ambience only)
        var xhr = new XMLHttpRequest();
        xhr.open("POST", "/", true);
        xhr.setRequestHeader('Content-Type', 'application/json');
        xhr.send(JSON.stringify({'play': this.id}));
    };
}