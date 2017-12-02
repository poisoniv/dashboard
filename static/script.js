function formatDate(date) {
  let hours = date.getHours();
  let minutes = date.getMinutes();
  const ampm = hours >= 12 ? 'pm' : 'am';
  hours %= 12;
  hours = hours || 12;
  minutes = minutes < 10 ? `0${minutes}` : minutes;
  const strTime = `${hours}:${minutes} ${ampm}`;
  return `${date.getMonth() + 1}/${date.getDate()}/${date.getFullYear()} ${strTime}`;
}

const NetworkStatus = {
  settings: {
    updateInterval: 30,
    networkTableHead: '<thead class="dark"><tr><th>Network Name</th><th>Status</th></tr></thead>',
  },
  el: {
    lastUpdatedDisplay: $('#last_updated'),
    networkTable: $('#network_status'),
  },
  init() {
    this.fetch_network_status();
    this.startTimer();
  },
  startTimer() {
    setInterval(this.fetch_network_status.bind(this), this.settings.updateInterval * 1000);
  },
  fetch_network_status() {
    this.el.lastUpdatedDisplay.html('Last Updated: Updating now...');
    $.ajax({
      async: true,
      url: '/fetch_all',
    }).done(this.network_status_handler.bind(this));
  },
  network_status_handler(result) {
    this.el.networkTable.html(this.settings.networkTableHead);
    result.forEach(this.tableAppender.bind(this));

    this.el.lastUpdatedDisplay.html(`Last Updated: ${formatDate(new Date())}`);
  },
  tableAppender(network) {
    let status = 'status_';
    if (network.status === 'Up') {
      status += 'up';
    } else {
      status += 'down';
    }
    this.el.networkTable.html(`${this.el.networkTable.html()}<tr><th>${network.name}</th><th><div class="${status}"></div>${network.status}</th></tr>`);
  },

};

NetworkStatus.init();
