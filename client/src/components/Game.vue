<template>
  <div>
    <b-container>
      <b-row class="text-center">
        <b-col></b-col>
        <b-col> 
          <div class="game-board">
          <div class="cell" v-for="mora in moras" v-if="mora.length === 3"  v-on:click="clicked_i(mora, i, form)">{{mora[i]}}</div>
          <div class="cell" v-else-if="mora.length === 2" v-on:click="clicked_j(mora, j, form)">{{mora[j]}}</div>
          <div class="cell" v-else v-on:click="form.word += mora[0]">{{mora[0]}}</div>
          </div>
        </b-col>
        <b-col></b-col>
      </b-row>
      <b-row class="text-center">
        <b-col> <h5>Score: {{max_score}} </h5></b-col>
        <b-col cols="6"></b-col>
        <b-col> <h5>Lives: {{ lives }} </h5></b-col>
      </b-row>
        <b-col> </b-col>
      </b-row>
      <b-row class="text-center">
        <b-col><h2 v-if="this.msg">{{msg}}</h2></b-col>
      </b-row>
      <b-row class="text-center">
        <b-col><div v-if="dictionary_output != 'Not a word'" v-for="(key,value) in dictionary_output"
                    >{{value}}: {{key}}</div>
        </b-col>
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
            <b-button type="submit" variant="primary">Enter</b-button>
            <b-button variant="danger">New </b-button>
            <b-button variant="warning" v-on:click="form.word = ''"> Reset </b-button>
          </b-form>
          </b-col>
        <b-col>
          <span>Words you've found: </span>
          <li v-for="n in used"> {{n}} </li>
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
  name: 'Game',
  data() {
    return {
      form: {
        word: '',
        hidden: '',
      },
      show: true,
      moras: '',
      i: 0,
      j: 0,
      numClicks: 0,
      dictionary_output: '',
      used: [],
      lives: 3,
      msg: '',
      cur_score: 0,
      max_score: 0,
    };
  },
  methods: {
    clicked_i(mora, i, form) {
      this.numClicks += 1; 
        if (this.numClicks == 1){
          var self = this;
          setTimeout(function(){
            switch(self.numClicks){
                case 1:
                  form.word += mora[i];
                  break;
                default:
                  if (self.i < 2)
                    self.i += 1;
                  else
                    self.i = 0;
            }
            self.numClicks = 0;
          }, 200);
        }
    }, 
    clicked_j(mora, j, form) {
      this.numClicks += 1; 
        if (this.numClicks == 1){
          var self = this;
          setTimeout(function(){
            switch(self.numClicks){
                case 1:
                  form.word += mora[j];
                  break;
                default:
                  if (self.j < 1)
                    self.j += 1;
                  else
                    self.j = 0;
            }
            self.numClicks = 0;
          }, 200);
        }
    },
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
            this.msg = 'X';
            this.dictionary_output == '';
            this.lives -= 1;
          }
          else if (check.includes(check_word))
          {
            this.msg = 'You have already tried using ' + check_word; 
            this.dictionary_output == '';
            this.lives -= 1;
          }
          else
          {
          this.msg = '正解';
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
    }
  },
  created() {
    this.getMoras();
  },
};
</script>

<style scoped>
li {
  list-style-type: none;
}

.game-board {
    display: grid;
    grid-template-rows: 50px 50px 50px;
    grid-template-columns: 50px 50px 50px;
}

.cell {
  background: grey;
  margin: 2px;
  color: #FFF;
  display: flex;
  align-items: center;
  justify-content: center;
  -webkit-touch-callout: none; 
    -webkit-user-select: none; 
     -khtml-user-select: none; 
       -moz-user-select: none; 
        -ms-user-select: none; 
            user-select: none; 
}

</style>
