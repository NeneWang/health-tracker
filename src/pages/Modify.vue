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
        msg: "demo of jsoneditor",
      }
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
