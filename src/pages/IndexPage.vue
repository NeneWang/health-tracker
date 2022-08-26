<template>
  <q-page class="flex flex-center">
    <!-- <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    > -->

    <img src="~assets/habit-track.gif" alt="this slowpoke moves" width="250" />
    <div class="q-pa-md">
      <form ref="form" @submit.prevent="postData">
        <div class="q-pb-md" v-for="(item, key) in fieldsConfig" :key="item.id">
          <!-- {{ parentMessage }} - {{ index }} - {{ item.message }} -->
          <b>
            {{ key }}
          </b>

          <div class="" v-if="item.type == 'TEXT'">
            <p>{{ item.value }}</p>
          </div>

          <dir class="text-left" v-if="item.type == 'NUMBER'">
            <q-input
              type="number"
              filled
              @change="printData(item.id)"
              v-model="$data[item.id]"
              :label="item.value"
            />
          </dir>

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
                :label="listItem"
              />
            </li>
            <!-- <div class="q-px-sm">
              The model data: <strong>{{ checkedList }}</strong>
            </div> -->
          </div>
        </div>
        <q-btn @click="postData"> Upload </q-btn>
      </form>
      <!-- <q-checkbox v-model="val" />  -->
    </div>
  </q-page>
  <div class="q-px-sm">
    <div class="text-weight-bolder">Log:</div>
    Date <strong>{{ date }}</strong> The model data:
    <strong>{{ checkedList }}</strong>
    Text {{ inputText }}
  </div>
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
    value: "Enter the block count",
    id: "2",
  },
  "How many miles?": {
    type: "NUMBER",
    value: "Enter miles ran",
    id: "1",
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

// Creat proper ids and also create the refs for the variables
const inputSetupList = Object.keys(fieldsConfig).reduce(function (
  filtered,
  key
) {
  // console.log(fieldsConfig[key].id)\
  fieldsConfig[key]["id"] = key.replace(/[^a-z0-9]/gi, "");
  if (fieldsConfig[key].type == "NUMBER") {
    filtered[fieldsConfig[key]["id"]] = ref();
  }

  return filtered;
},
{});

console.log(inputSetupList, fieldsConfig);

const setupConfig = {
  val: ref(false),
  model: ref(2),
};

export default defineComponent({
  name: "IndexPage",
  setup() {
    return {
      ...setupConfig,
      ...inputSetupList,
      date: ref(utc),
      checkedList: ref([]),
    };
  },
  data() {
    return {
      fieldsConfig: { ...fieldsConfig },
    };
  },
  computed() {},
  methods: {
    printData: function (data) {
      console.log(data, this.$data[data]);
    },
    postData: function (data) {
      const returnObject = {
        checkedList: this.checkedList,
        inputField: Object.keys(inputSetupList).map((inputKey) => {
          const myobj = {};
          myobj[inputKey] = this.$data[inputKey];
          return myobj;
        }),
      };

      const examplePostBody = {
        user_id: '1',
        date: this.date,
        data: returnObject
      }

      console.log("POST REQUEST", JSON.stringify(examplePostBody));
    },
  },
});

// .map( keyInput => this.$data[keyInput] )
</script>
