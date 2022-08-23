<template>
  <q-page class="flex flex-center">
    <div class="q-pa-md" style="max-width: 500px">
      Modify Habits
      <q-input v-model="habitsSetting" filled type="textarea" />
      <vue-json-editor
        v-model="habitsSetting"
        mode="code"
        :show-btns="true"
        :expandedOnStart="true"
        @json-change="onJsonChange"
      ></vue-json-editor>
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
      json: {
        msg: "demo of jsoneditor",
      },
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
  },
});
</script>
