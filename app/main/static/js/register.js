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
            base_id: null,
            target_id: null,
            area_id: null
        },
        computed: {
            isBaseSelected: function() {
                return this.examsData[this.base_id] !== undefined;
            },
            isTargetSelected: function() {
                return this.isBaseSelected && this.examsData[this.target_id] !== undefined;
            },
            isAreaSelected: function() {
                return this.isTargetSelected && this.examsData[this.target_id].areas[this.area_id] !== undefined;
            },
            availableTargets: function(){
                available = [];

                this.examsData.forEach(element => {
                    if (element.weight <= this.examsData[this.base_id].weight || element.weight == this.examsData[this.base_id].weight + 1) {
                        available.push(element);
                    }
                });

                return available
            }
        }
    })
}