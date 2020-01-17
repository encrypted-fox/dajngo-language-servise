/* App.js */
var React = require('react');
var ReactDOM = require('react-dom');
var Component = React.Component;
import axios from 'axios';
import * as CanvasJSReact from './canvasjs.react';

var CanvasJS = CanvasJSReact.CanvasJS;
var CanvasJSChart = CanvasJSReact.CanvasJSChart;

export default class App extends Component {

    constructor(props) {
        super(props);
        this.state = {"dots": []}
    }


    loadData() {
        let arr = [];
        axios.get("http://127.0.0.1:8000/api/v0/logging").then(results => {
            return results
        }).then(data => {
            arr = data.data;
            console.log(arr);

            let obj = {};

            for (let i = 0; i < arr.length; i++) {
                if (!obj.hasOwnProperty(arr[i]["req_type"]) && arr[i]['req_type'] != "GET /api/v0/logging/" && arr[i]['req_type'] != '' ) {
                    obj[arr[i]["req_type"]] = 1
                } else if (obj.hasOwnProperty(arr[i]["req_type"])) {
                    obj[arr[i]["req_type"]] += 1
                }
            }

            let dots = [];
            for (let key in obj) {
                dots.push({"label": key, "y": obj[key]})
            }
            this.setState({"dots": dots})
            console.log(dots)
        });
    }

    componentDidMount() {
        this.loadData();
        this.intervalId = setInterval(() => this.loadData(), 2500);
    }

    componentWillUnmount() {
        clearInterval(this.intervalId);
    }

    render() {

        const options = {
            animationEnabled: true,
            theme: "light",
            title: {
                text: "Посещения"
            },
            axisY: {
                title: "Количество посещений",
                scaleBreaks: {
                    autoCalculate: false,
                    type: "wavy",
                    lineColor: "white"
                }
            },
            data: [{
                type: "column",
                indexLabel: "{y}",
                indexLabelFontColor: "white",
                dataPoints: this.state.dots
            }]
        };

        return (
            <div>
                <CanvasJSChart options={options}
                />
            </div>
        );
    }
}

ReactDOM.render(<App/>, document.getElementById('app'));