<template>
  <apexchart
    height="300"
    type="heatmap"
    :options="options"
    :series="series"
  ></apexchart>
</template>

<script>
import { defineComponent } from "vue";
import { getCssVar } from "quasar";

export default defineComponent({
  name: "Habits Heatmap",
  data() {
    return {
      options: {
        title: {
          text: "Habits Heatmap",
          align: "left",
        },
        chart: {
          id: "apex-column",
        },
        colors: [
          getCssVar("primary"),
          getCssVar("secondary"),
          getCssVar("negative"),
        ],
        xaxis: {
          categories: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        },
        plotOptions: {
          bar: {
            horizontal: false,
            columnWidth: "55%",
            endingShape: "rounded",
          },
        },
      },
      series: [
        { name: "Productivity blocks completed", data: [5, 2, 3, 4, 5, 2, 2] },
        { name: "Running", data: [3, 2, 0, 0, 3, 2, 7] },
      ],
    };
  },
});
</script>
