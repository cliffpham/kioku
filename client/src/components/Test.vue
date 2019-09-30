<template>
  <div>
    <b-container>
      <b-row class="text-center">
        <b-col> <h3>Score: {{max_score}} </h3></b-col>
        <b-col> <h1> {{moras}} </h1></b-col>
        <b-col> <h3>Lives: {{ lives }} </h3></b-col>
      </b-row>
      <b-row class="text-center">
        <b-col><h2>{{msg}}</h2></b-col>
      </b-row>
      <b-row class="text-center">
        <b-col><h6>{{dictionary_output}}</h6></b-col>
      </b-row>
      <b-row>
        <b-col>
          <b-form @submit="onSubmit" v-if="show">
            <b-form-group
              id="input-group-1"
              label="Word:"
              label-for="input-1"
            >
              <b-form-input
                id="input-1"
                v-model="form.word"
                type="word"
                placeholder="Enter word"
              ></b-form-input>
            </b-form-group>
            <b-button type="submit" variant="primary">Submit</b-button>
          </b-form>
          </b-col>
        <b-col>
          <p> {{used}} </p>
        </b-col>
      </b-row>
    </b-container>
    <b-card class="mt-3" header="Form Data Result">
      <pre class="m-0">{{ form }}</pre>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      form: {
        word: '',
        hidden: '',
      },
      show: true,
      moras: '',
      dictionary_output: '',
      used: [],
      lives: 3,
      msg: '',
      cur_score: 0,
      max_score: 0,
    };
  },
  methods: {
    getMoras() {
      const path = 'http://localhost:5000/test';
      axios.get(path)
        .then((res) => {
          this.moras = res.data.moras;
          this.form.hidden = res.data.hidden;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    pipeWord(payload) {
      const path = 'http://localhost:5000/check';
      axios.get(path, { params: payload })
        .then((res) => {
          this.dictionary_output = res.data;
          const check = this.used;
          const check_word = this.form.word;
          if (this.dictionary_output == "Not a word")
          {
            this.msg = 'This is not a word!';
            this.lives -= 1;
          }
          if (check.includes(check_word))
          {
            this.msg = 'You have already tried using ' + check_word; 
            this.lives -= 1;
          }
          else
          {
          this.msg = 'Correct!';
          this.max_score += 1;
          this.used.push(this.form.word);
          this.resetForm();
          }
        });
    },
    onSubmit(evt) {
      evt.preventDefault();
      const payload = this.form;
      this.pipeWord(payload);
    },
    resetForm() {
      this.form.word = '';
      this.msg = '';
    }
  },
  created() {
    this.getMoras();
  },
};
</script>
