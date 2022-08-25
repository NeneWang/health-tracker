<template>
  <q-page class="flex flex-center">
    <!-- <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    > -->

    <img src="~assets/habit-track.gif" alt="this slowpoke moves" width="250" />
    <div class="q-pa-md">
      <form action="">
        <div class="q-pb-md" v-for="(item, key) in fieldsConfig" :key="item.id">
          <!-- {{ parentMessage }} - {{ index }} - {{ item.message }} -->
          <b>
            {{ key }}
          </b>

          <div v-if="item.type == 'TEXT'">
            <p>{{ item.value }}</p>
          </div>

          <div v-if="item.type == 'DATETIME'">
            <div class="q-gutter-md row items-start">
              <q-date v-model="date" minimal />
            </div>
          </div>

          <div v-if="item.type == 'CHECKBOX'">
            <li v-for="listItem in item.list" :key="listItem">
              <q-checkbox
                type="checkbox"
                v-model="checkedList"
                :val="listItem"
              />
              <label :for="listItem"> {{ listItem }}</label>
            </li>
            <!-- <div class="q-px-sm">
              The model data: <strong>{{ checkedList }}</strong>
            </div> -->
          </div>
        </div>
      </form>

      <div class="q-px-sm">
        Other Data <strong>{{date}}</strong>
        The model data: <strong>{{ checkedList }}</strong>
      </div>
      <!-- <q-checkbox v-model="val" />  -->
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from "vue";
import { ref } from "vue";
var utc = new Date().toJSON().slice(0, 10).replace(/-/g, "/");
// document.write(utc);
var fieldsConfig = {
  "Daily Plan": {
    type: "TEXT",
    value: "5am Wake up and Train",
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
};

const setupConfig = {
  val: ref(false),
  model: ref(2),
};

export default defineComponent({
  name: "IndexPage",
  setup() {
    return {
      ...setupConfig,
      date: ref(utc),
      checkedList: ref([]),
    };
  },
  data() {
    return {
      fieldsConfig: { ...fieldsConfig },
    };
  },
});
</script>
