<template>
  <q-page>
    <div>
      Modify Habits
      <!-- <q-input v-model="habitsSetting" filled type="textarea" /> -->
      <vue-json-editor
        v-model="json"
        :mode="'code'"
        :value="value"
        @json-change="onJsonChange"
      >
      </vue-json-editor>

      <button type="button" @click="resetJson">reset</button>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import vueJsonEditor from "vue-json-editor";

export default {
  data() {
    return {
      value: {
        "Daily Habits": {
          type: "TEXT",
          value: "Wake up and trainning",
        },
        "DAY - What day is this report for?": { type: "DATETIME" },
        "BLOCKS - How much Time blocks were you able to complete?": {
          type: "NUMBER",
        },
        "Systems Applied ✅": {
          type: "CHECKBOX",
          list: ["Trainning while doing algorithms", "Running on the mornings"],
        },
        "Vices 🙈": {
          type: "CHECKBOX",
          list: [
            "Railed off from my Gaming Strategy",
            "Slept on the Afternoon (Before Bed Time)",
            "Hard Break",
          ],
        },
        "Achievements 🏆": {
          type: "CHECKBOX",
          list: [
            "1+ Algo/Problem/topic explained 🍃👨‍💼",
            "Reading Done 📚",
            "Workout routine gym 💪",
            "5+features Github 🐱‍💻",
            "2+ features on Personal Project 🐱‍👤👺",
          ],
        },
      },
    };
  },

  components: {
    vueJsonEditor,
  },
  methods: {
    onJsonChange(value) {
      console.log("value:", value);
    },
  },
};
</script>
