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
          value:
             "5:45am - 6:15am   | Wake-up -> Brush up teeth -> Prepare -> Go to bus stop.\
              6:15am - 8:00am  | Go To Office | Do Anki/Readings on your way.\
              8 :05am -9:00am   | Udemy: Related to Job\
              9:00am  - 5:45pm | Work\
              5:48pm - 7:30pm | Travel\
              7:45pm - 8:30pm | Take a Bath, Eat, and do ASVAB\
              8:30pm - 9:30pm | Start Pomodoro Blocks (Obj:6) Algorithms while Working Out\
              9:30pm - 10:30pm | Buffer + 5 Udemy (10pm) + 2 Features Personal Project (10:30pm)",
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
