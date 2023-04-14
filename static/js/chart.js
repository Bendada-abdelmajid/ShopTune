const displayChart = (data, labels, text) => {
    const ctx = document.getElementById('myChart').getContext('2d');
    let gradient=ctx.createLinearGradient(0, 0, 0, 400);
    gradient.addColorStop(0, "rgb(140, 190, 247)");
    gradient.addColorStop(1, "rgb(140, 190, 107)");
    var myChart = new Chart(ctx, {
      type: 'line',
      data: {
        labels: labels,
        datasets: [
          {
            label: '',
            data: data,
            backgroundColor:gradient,
            borderColor: [
              "rgba(255, 99, 132, 1)",
              "rgba(54, 162, 235, 1)",
              "rgba(255, 99, 132,0.7)",
              "rgba(75, 192, 192, 1)",
            ],
            borderWidth: 1,
          },
        ],
      },
      options: {
        maintainAspectRatio: true,
        title: {
          display: true,
          text:"Best 10 Orders this" + text ,
          fontSize: 20,
        },
       
        legend: {
          display: false,
          
        },
      },
    });
  };
  
  const getCategoryData = (e, date, text) => {
    
    console.log("fitching");
    fetch("/shopkeeper/order_category_summary/" +date )
      .then((res) => res.json())
      .then((res1) => {
        const results = res1.order_data;
        const [labels, data] = [Object.keys(results), Object.values(results)];
        console.log("data", data);
        displayChart(data, labels, text);
        e.parentElement.querySelector('.active').classList.remove('active')
        e.classList.add('active')
      });
  

  };

document.onload=  getCategoryData(document.querySelector('.chart-container .active'),"week", 'week');
