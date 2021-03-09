var obj = document.getElementById("myChart").getContext("2d");

var myChart = new CanvasJS.Chart(obj,{
    title :{
        text :"Multiple Y Axis Chart"
    },
    axisY:[
        {
            title: " Axis Y 1 Title",
        },
        {
            title: " Axis Y 2 Title",
        },
    ],
    data: [{
        type: "line",
        axisYIndex: 0,
        dataPoints: [
            {label:"apple",y:10 },
            {label:"orange",y:9 },
            {label:"mango",y:16 },
            {label:"greps",y:25 },
            {label:"chili",y:28 },
        ],
        },
        {
        type:"column",
        axisYIndex:1,
        dataPoints:[
            {label:"apple",y:10 },
            {label:"orange",y:9 },
            {label:"mango",y:16 },
            {label:"greps",y:25 },
            {label:"chili",y:28 },
        ]
        },   
    ],
    options: {
        responsive: false,
        },
            animation:{
            duration:5000,
            easing: "easeOutQuint",
        }
    },
});

chart.render();