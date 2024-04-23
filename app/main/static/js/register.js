function getExamsData() {
    let examsData = document.getElementById("exams-data").innerHTML;
    let examsDataJSON = JSON.parse(examsData);

    return examsDataJSON
}

window.onload = function() {
    var a = new Vue({
        el: '.exams-form',
        data: {
            examsData: getExamsData(),
            base: "0",
            target: "0",
            area: "0",
        },
        computed: {
            isBaseSelected: function() {
                return this.base !== "0"
            },
            isTargetSelected: function() {
                return this.isBaseSelected && this.target !== "0"
            },
            isAreaSelected: function() {
                return this.isTargetSelected && this.area !== "0"
            },
            availableTargets: function(){
                available = [];

                this.examsData.forEach(element => {
                    if (element.weight <= this.base.weight || element.weight == this.base.weight + 1) {
                        available.push(element);
                    }
                });

                return available
            }
        }
    })
}