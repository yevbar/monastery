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
        let question = document.getElementById("question").value;
        console.log("We're in the askQuestion method where the question is " + question);
		    this.setState({question: question, ask: false}, this.requestAnswer(question));
	  }

    requestAnswer = (question) => {
        console.log("We're going to be posting the question: " + question);
        // here we're going to make a request to the server with the question text (probably in json format) and receive the answer to the question
        fetch('/question', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                question: question,
            })
        })
            .then(res => res.json())
            .then(data => this.setState({answer: data.answer}));
    }

    askAgain = (event) => {
        this.setState({ask: true, question: null});
    }

	render() {
		return (
			<div style={{display: "flex", justifyContent: "center", alignItems: "center"}}>
			{
				  this.state.ask ? <form onSubmit={this.askQuestion} autoComplete="off" style={{display: "flex", justifyContent: "center", alignItems: "center", flexDirection: "column"}}>
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
