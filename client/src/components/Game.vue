<template>
  <div>
    <GlobalEvents @keydown.enter="onSubmit"></GlobalEvents>
    <b-container>
      <b-row class="text-center">
        <b-col>
        <b-col><h2 v-if="this.msg">{{msg}}</h2></b-col>
        </b-col>
      </b-row>
      <b-row id="test" class="text-center">
        <b-col> <h5>Score: {{max_score}} </h5></b-col>
        <b-col cols="6"></b-col>
        <b-col> <h5>Lives: {{ lives }} </h5></b-col>
      </b-row>
        <b-col> </b-col>
      </b-row>
      <b-row id="display" class="text-center">
        <b-col><div v-if="dictionary_output != 'Not a word'" v-for="(key,value) in dictionary_output"
                    >{{value}}: {{key}}</div>
        </b-col>
      </b-row>
      <b-row class="selector">
        <b-col>
          <div class="game-board">
          <div class="cell" v-for="mora in moras" v-if="mora.length === 3"  v-on:click="clicked_i(mora, i, form)">{{mora[i]}}</div>
          <div class="cell" v-else-if="mora.length === 2" v-on:click="clicked_j(mora, j, form)">{{mora[j]}}</div>
          <div class="cell" v-else v-on:click="form.word += mora[0]">{{mora[0]}}</div>
          </div>
          <b-form @submit="onSubmit" v-if="show">
            <b-form-group
              id="input-group-1"
              label-for="input-1"
            >
              <input
                v-on:keyup="test"
                id="input-1"
                v-model="form.word"
                type="word"
                placeholder="言葉を作ってみて"
              ></input>
            </b-form-group>
            <div class="buttons">
              <div class="buttonCell" v-on:click="onSubmit">入力</div>
              <div class="buttonCell" v-on:click="deleteChar"> 消 </div>
              <div class="buttonCell"> 新 </div>
              <div class="buttonCell" v-on:click="form.word = ''"> R </div>
              <div class="buttonCell"> 変更</div>
            </div>
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
      msg: '言葉を探そう!',
      cur_score: 0,
      max_score: 0,
    };
  },
  methods: {
    test(evt) {
      console.log(evt.key);
    },
    deleteChar() {
      let str = this.form.word;
      console.log(str);
      const lastIndex = str.length - 1;
      str = str.substring(0, lastIndex);

      this.form.word = str;
    },
    clicked_i(mora, i, form) {
      this.numClicks += 1;
      if (this.numClicks == 1) {
        const self = this;
        setTimeout(() => {
          switch (self.numClicks) {
            case 1:
              form.word += mora[i];
              break;
            default:
              if (self.i < 2) self.i += 1;
              else self.i = 0;
          }
          self.numClicks = 0;
        }, 200);
      }
    },
    clicked_j(mora, j, form) {
      this.numClicks += 1;
      if (this.numClicks == 1) {
        const self = this;
        setTimeout(() => {
          switch (self.numClicks) {
            case 1:
              form.word += mora[j];
              break;
            default:
              if (self.j < 1) self.j += 1;
              else self.j = 0;
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
          if (this.dictionary_output == 'Not a word') {
            this.msg = 'X';
            this.dictionary_output == '';
            this.lives -= 1;
          } else if (check.includes(check_word)) {
            this.msg = `You have already tried using ${check_word}`;
            this.dictionary_output == '';
            this.lives -= 1;
          } else {
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
    },
  },
  created() {
    this.getMoras();
    document.onkeydown.enter = this.onSubmit();
  },
};
</script>

<style scoped>
input {
  width: 224px;
  border: 0px solid;
}
li {
  list-style-type: none;
}

#test {
  border-bottom: solid 2px grey;
  margin-bottom: 15px;
}

#display {
  padding-bottom: 15px;
}

.selector {
  border-top: solid 2px grey;
  padding-top: 15px;
}

.buttons {
  display: grid;
  grid-template-rows: 30px;
  grid-template-columns: 41px 41px 41px 41px 41px;
}

.buttonCell {
  background: lightgrey;
  display: flex;
  align-items: center;
  margin: 2px;
  justify-content: center;
}

.game-board {
    display: grid;
    grid-template-rows: 75px 75px 75px;
    grid-template-columns: 75px 75px 75px;
}

.cell {
  background: grey;
  margin: 2px;
  font-size: 2em;
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
