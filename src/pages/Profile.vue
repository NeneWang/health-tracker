<template>
  <!-- <q-page class="flex flex-center"> Profile </q-page> -->
  <q-card>
    <apex-column />
  </q-card>
</template>

<script>
import { defineComponent, defineAsyncComponent } from 'vue'

const ApexBar = defineAsyncComponent(() =>
  import('src/components/charts/ApexBar.vue')
)

const ApexColumn = defineAsyncComponent(() =>
  import('components/charts/ApexColumn.vue')
)

const ApexLine = defineAsyncComponent(() =>
  import('components/charts/ApexLine.vue')
)

const ApexDonut = defineAsyncComponent(() =>
  import('components/charts/ApexDonut.vue')
)

const ApexCandlestick = defineAsyncComponent(() =>
  import('components/charts/ApexCandlestick.vue')
)

const ApexArea = defineAsyncComponent(() =>
  import('components/charts/ApexArea.vue')
)

const ApexBubble = defineAsyncComponent(() =>
  import('components/charts/ApexBubble.vue')
)
const HeatMapChart = defineAsyncComponent(()=>{
  import('components/charts/HeatMapChart.vue')
})

// const app = createApp(App);

export default defineComponent({
  name: "profilePage",
  components: {
    // HeatMap,
    HeatMapChart,
    ApexBar,
    ApexLine,
    ApexColumn,
    ApexDonut,
    ApexCandlestick,
    ApexArea,
    ApexBubble,
  },
});
</script>
