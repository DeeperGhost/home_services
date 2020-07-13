$(document).ready(function(){
    //form Submit action
    $("form#data").submit(function(event){
        //disable the default form submission
        event.preventDefault();
        //grab all form data
        var formData = new FormData($(this)[0]);

        function setProgress(e) {
            if (e.lengthComputable) {
                var complete = e.loaded / e.total;
                $("#pBar").text(Math.floor(complete*100)+"%");
//                                $("#pBar2").text({{count}});

            }
        }
        $.ajax({
            xhr: function() {
                var xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener("progress", setProgress, false);
                xhr.addEventListener("progress", setProgress, false);
                return xhr;
            },
//            url:"http://192.168.0.102:5000/test",
            url: "/upload",
            type: 'POST',
            data: formData,
            async: true,
            cache: false,
            contentType: false,
            processData: false,
            enctype: 'multipart/form-data',
            success: function (returndata) {
            $("#pBar2").text(returndata.count);
//                alert(returndata);
            }
        });
        return false;
    });
});
