
function get_data(url = "confirmed", csrf) {

  var options = {
    chart: {
      zoom: {
        enabled: true
      },
      height: 380,
      width: "100%",
      type: "area",
      animations: {
        initialAnimation: {
          enabled: true
        }
      }
    },
    dataLabels: {
      enabled: false,
      style: {
        colors: ['#333']
      },
    },
    series: [],
    theme: {
      monochrome: {
        enabled: true,
        color: '#255aee',
        shadeTo: 'light',
        shadeIntensity: 0.65
      }
    },

    xaxis: {
      type: "datetime"
    }
  };

  var chart = new ApexCharts(document.querySelector("#myChart"), options);
  chart.render();


  $.ajax({
    url: url,
    type: 'POST',
    data: {
      csrfmiddlewaretoken: csrf
    }
  })
    .done(function (res) {

      chart.updateOptions({
        theme: {
          monochrome: {
            enabled: true,
            color: res.color,
            shadeTo: 'light',
            shadeIntensity: 0.65
          }
        }
      })


      chart.updateSeries([{
        name: res.head,
        data: res.ans
      }])
    })
    .fail(function () {
      alert("failed");
    });
}





function get_data2(url = "total_confirmed", csrf) {

  var options = {
    chart: {
      zoom: {
        enabled: true
      },
      height: 380,
      width: "100%",
      type: "area",
      animations: {
        initialAnimation: {
          enabled: true
        }
      }

    },
    dataLabels: {
      enabled: false,
    },
    series: [
    ],
    theme: {
      monochrome: {
        enabled: true,
        color: '#A21F04',
        shadeTo: 'light',
        shadeIntensity: 0.65
      }
    },

    xaxis: {
      type: "datetime"
    },
  };

  var chart = new ApexCharts(document.querySelector("#myChart2"), options);
  chart.render();


  $.ajax({
    url: url,
    type: 'POST',
    data: {
      csrfmiddlewaretoken: csrf
    }
  })
    .done(function (res) {
      chart.updateOptions({
        theme: {
          monochrome: {
            enabled: true,
            color: res.color,
            shadeTo: 'light',
            shadeIntensity: 0.65
          }
        }
      })


      chart.updateSeries([{
        name: res.head,
        data: res.ans
      }], true)
    })
    .fail(function () {
      alert("failed");
    });
}


function active() {
  var current = document.getElementsByClassName("active");
  current.classList.remove("acive");
}


function get_state(csrf) {
  var val = document.getElementById("inputGroupSelect04");
  var name = val.value
  if (name == "Choose State") {
    name = "Madhya Pradesh";
  }
  $.ajax({
    url: 'state ',
    type: 'POST',
    data: {
      csrfmiddlewaretoken: csrf
    }
  })
    .done(function (res) {
      const old = Chart.getChart("pie-chart");
      if (old) {
        old.destroy();
      }
      new Chart(document.getElementById("pie-chart"), {
        type: 'pie',
        data: {
          labels: ["Active Cases", "Confirmed Cases", "Recovered Cases", "Deaths Cases"],
          datasets: [{
            label: "Number of Cases",
            backgroundColor: ["#06EEF7", "#F79806", "#9BF20C", "#781A06"],
            data: res[name].series
          }]
        },
        options: {
          title: {
            display: true,
            text: 'Covid 19 Statewise analysis'
          }
        }
      });

      var rrate = (res[name].series[2] / res[name].series[1]) * 100
      rrate = rrate.toFixed(3);
      document.getElementById("rrate").innerText = "Recovery rate : " + rrate + "%";
      var drate = (res[name].series[3] / res[name].series[1]) * 100
      drate = drate.toFixed(3);
      document.getElementById("drate").innerText = "Death rate : " + drate + "%";
    })
    .fail(function () {
      alert("failed");
    });

  document.getElementById("statename").innerText = name

}


