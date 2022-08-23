<template>
  <q-page class="flex flex-center">
    <!-- <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    > -->

    <img src="~assets/habit-track.gif" alt="this slowpoke moves" width="250" />
    <div class="q-pa-md">
      <div class="q-gutter-md" style="max-width: 500">
        <q-input
          borderless
          type="number"
          v-model.number="model"
          label="I ran __ miles 🏃‍♀️"
        />
      </div>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import { ref } from "vue";

export default defineComponent({
  name: "IndexPage",
  setup() {
    return {
      model: ref(2),
    };
  },
});
</script>
