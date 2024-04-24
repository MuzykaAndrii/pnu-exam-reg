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
            baseId: null,
            targetId: null,
            areaId: null
        },
        computed: {
            isBaseSelected: function() {
                return this.examsData.find((deg) => deg.id == this.baseId) !== undefined;
            },
            isTargetSelected: function() {
                return this.isBaseSelected && this.examsData.find((deg) => deg.id == this.targetId) !== undefined;
            },
            isAreaSelected: function() {
                return this.isTargetSelected && this.examsData.find((deg) => deg.id == this.targetId).areas.find((ar) => ar.id == this.areaId) !== undefined;
            },
            availableTargets: function(){
                let available = [];
                let base_weight = this.examsData.find((deg) => deg.id == this.baseId).weight;

                this.examsData.forEach(element => {
                    if (element.weight <= base_weight || element.weight == base_weight + 1) {
                        available.push(element);
                    }
                });

                return available;
            },

            availableAreas: function() {
                return this.examsData.find((deg) => deg.id == this.targetId).areas;
            },

            availableExams: function() {
                return this.examsData.find((deg) => deg.id == this.targetId).areas.find((ar) => ar.id == this.areaId).exams;
            }
        }
    })
}