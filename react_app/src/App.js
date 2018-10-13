import React from 'react';

class App extends React.Component {
	constructor(props) {
		super(props);
		this.state = {ask: true, question: null, answer: false};
		  this.askQuestion = this.askQuestion.bind(this);
      this.requestAnswer = this.requestAnswer.bind(this);
	}

	  askQuestion = (event) => {
        event.preventDefault();
		    this.setState({question:  document.getElementById("question").value, ask: false}, this.requestAnswer(this.state.question));
	  }

    requestAnswer = (question) => {
        // here we're going to make a request to the server with the question text (probably in json format) and receive the answer to the question
    }

    askAgain = (event) => {
        this.setState({ask: true, question: null});
    }

	render() {
		return (
			<div style={{display: "flex", justifyContent: "center", alignItems: "center"}}>
			{
				  this.state.ask ? <form onSubmit={this.askQuestion} autocomplete="off" style={{display: "flex", justifyContent: "center", alignItems: "center", flexDirection: "column"}}>
				<span>What would you like to know?</span>
				<input id="question" type="text" name="question"/>
				</form>
				: 
				      <div style={{display: "flex", justifyContent: "center", alignItems: "center", flexDirection: "column"}}>
              <span><b>{this.state.question}</b></span>
              <span>{this.state.answer ? this.state.answer : "Loading"}</span>
              <span onClick={this.askAgain} style={{color: "grey"}}><i>Ask another question</i></span>
              </div>
			}
			</div>
		);
	}
}

export default App;
