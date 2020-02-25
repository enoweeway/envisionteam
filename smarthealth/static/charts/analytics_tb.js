var SalesChart = (function () {

    // Variables

    var $chart = $('#chart-sales');


    // Methods

    function init($this) {
        var salesChart = new Chart($this, {
            type: 'line',
            options: {
                scales: {
                    yAxes: [{
                        gridLines: {
                            color: Charts.colors.gray[200],
                            zeroLineColor: Charts.colors.gray[200]
                        },
                        ticks: {

                        }
                    }]
                }
            },
            data: {
                labels: [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018],
                datasets: [{
                    label: 'Performance',
                    data: [590, 579, 569, 559, 549, 539, 530, 520, 524, 528, 531, 535, 539, 543, 546, 550, 554, 554, 554]
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