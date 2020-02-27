var SalesChart = (function () {

    // Variables

    var $chart = $('#total_patients');


    // Methods

    function init($this) {
        var salesChart = new Chart($this, {
            type: 'line',
            options: {
                scales: {
                    yAxes: [{
                        gridLines: {
                            color: Charts.colors.gray[700],
                            zeroLineColor: Charts.colors.gray[700]
                        },
                        ticks: {

                        }
                    }]
                }
            },
            data: {
                labels: ['May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
                datasets: [{
                    label: 'Clients',
                    data: [0, 20, 10, 30, 15, 40, 20, 60]
                }]
            }
        });

        // Save to jQuery object

        $this.data('chart', salesChart);

    };


    // Events

    if ($chart.length) {
        init($chart);
    }

})();