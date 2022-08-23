<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md" style="max-width: 500px">
      Modify Habits
      <q-input v-model="habitsSetting" filled type="textarea" />
      <vue-json-editor
        v-model="json"
        :show-btns="true"
        :mode="'code'"
        lang="zh"
        @json-change="onJsonChange"
        @json-save="onJsonSave"
        @has-error="onError"
      >

      
      </vue-json-editor>

      <button type="button" @click="resetJson">reset</button>
    </div>
  </q-page>
</template>

<script>
import { defineComponent, ref } from "vue";
import vueJsonEditor from "vue-json-editor";

export default defineComponent({
  name: "modifyPage",
  components: {
    vueJsonEditor,
  },
  data() {
    return {
      json: [{ name: "Dirk", age: 1234 }, { name: "Jason" }],
    };
  },
  setup() {
    return {
      habitsSetting: ref("{'sadasd': true}"),
    };
  },
  methods: {
    onJsonChange(value) {
      console.log("value:", value);
    },
    onJsonSave(value) {
      console.log("value:", value);
    },
    onError(value) {
      console.log("value:", value);
    },
    resetJson() {
      this.json = [{ name: "Dirk", age: 1234 }, { name: "Jason" }];
    },
  },
});
</script>
