<template>
  <q-page>
    <div>
      Modify Habits
      <!-- <q-input v-model="habitsSetting" filled type="textarea" /> -->

      <!-- <button type="button" @click="resetJson">reset</button> -->
      <br />
      <br />
      <!-- <q-btn type="button" @click="uploadSettings">Save</q-btn> -->

      <br />
      <vue-json-editor
        v-model="json"
        :mode="'code'"
        :value="settings"
        style="min-height: 500px"
        @json-change="onJsonChange"
      >
      </vue-json-editor>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import vueJsonEditor from "vue-json-editor";

export default {
  data() {
    return {
      settings: {
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

  beforeMount() {
    console.log("before");
    fetch(`http://127.0.0.1:5000/settings?user_id=1`).then((response) => response.json())
  .then((data) => {
    console.log(JSON.parse(data.data))
    this.settings = JSON.parse(data.data)
    console.log(data)});

  },
  components: {
    vueJsonEditor,
  },
  methods: {
    onJsonChange(value) {
      // this.uploadSettingsSpecific(value)
      console.log("settings:", value);
      this.uploadSettingsSpecific(value)
    },
    uploadSettings() {
      const uploadObject = {
        user_id: 1,
        data: JSON.stringify(this.settings),
      };

      console.log("POSTING", JSON.stringify(uploadObject));

      const requestOptions = {
        method: "PUT",
        // params: uploadObject,
      };
      fetch(
        `http://127.0.0.1:5000/settings?user_id=1&data=${uploadObject.data}`,
        requestOptions
      ).then((response) => response.json());
    },
    uploadSettingsSpecific(data) {

      console.log("POSTING", data);

      const requestOptions = {
        method: "PUT",
        // params: uploadObject,
      };
      fetch(
        `http://127.0.0.1:5000/settings?user_id=1&data=${JSON.stringify(data)}`,
        requestOptions
      ).then((response) => response.json());
    },
  },
};
</script>

<style>
.ace_editor {
  height: 60em !important;
}
/* ace_gutter-layer ace_folding-enabled */
.ace_layer {
  height: 60em !important;
}
</style>
