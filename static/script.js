var networkTableHead = "<tr><th>Network Name</th><th>Status</th></tr>"
var updateInterval = 30 // In seconds

function fetch_network_status(){
    $('#last_updated').html("Last Updated: Updating now...")
    $.ajax({
        url: '/fetch_all'
    }).done(network_status_handler)

}

function network_status_handler(network_statuses){
    console.log(network_statuses)
    var networkTable = $("#network_status")
    networkTable.html(networkTableHead)


    network_statuses.forEach(function(network){
        var status = 'status_'
        if (network.status == "Up"){
             status += 'up'
        } else {
             status +='down'
        }
        networkTable.html(networkTable.html()+'<tr><th>'+network.name+'</th><th><div class="'+status+'"></div>'+network.status+'</th></tr>')
    })

     $('#last_updated').html("Last Updated: "+formatDate(new Date))
}

function formatDate(date) {
  var hours = date.getHours();
  var minutes = date.getMinutes();
  var ampm = hours >= 12 ? 'pm' : 'am';
  hours = hours % 12;
  hours = hours ? hours : 12;
  minutes = minutes < 10 ? '0'+minutes : minutes;
  var strTime = hours + ':' + minutes + ' ' + ampm;
  return date.getMonth()+1 + "/" + date.getDate() + "/" + date.getFullYear() + " " + strTime;
}

fetch_network_status()

setInterval(fetch_network_status, updateInterval * 1000)