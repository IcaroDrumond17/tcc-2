function Send(e) {
    if (e.keyCode == 13) {
        perguntar();
        return false; // para n recarregar a page novamente
    }
}

function perguntar() {
    const input = document.getElementById('input');
    const question = input.value.toString().trim(); // trim elimina espaços
    // remove acentos
    let questionSEND = question.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    // remove caracteres não alfanumericos
    questionSEND = questionSEND.replace(/[^a-zA-Z0-9@,.;:!-?\s]/g, '');

    const msg = document.getElementById('msg');
    const code_before = document.getElementById('code_before');

    let msgLines = msg.innerHTML;
    msgLines = msgLines.replace('<a href="#" id="end">', '');

    const codBefore = Number(code_before.value);

    const http = new XMLHttpRequest();
    // envio assicrono
    http.open('GET', `/chatbot/input/${codBefore}/${questionSEND}`, true);
    http.setRequestHeader('Content-Type', 'aplication/x-www-form-urlencoded');

    // lendo o estado de alteração do objeto http
    http.onreadystatechange = function () {
        if (this.readyState === XMLHttpRequest.DONE && this.status === 200) {
            // se o estado foi concluido
            let objJSON = JSON.parse(http.responseText);
            if (objJSON.length > 0) {
                code_before.value = objJSON[0].code_current;

                const input_question = question;
                const output = objJSON[0].output.toString().trim();
                // balões
                msgLines += `
                <div class="row">
                    <div class="col align-self-end">
                        <div class="talk-bubble talk-ballon-right balloon-right" style="background-color: #8000ff;">
                            <div class="talktext text-right">
                                <p>${input_question}</p>
                            </div>
                        </div> 
                    </div>
                </div> 
            
                <div class="row">
                    <div class="col align-self-start">
                        <div class="talk-bubble talk-ballon-left balloon-left" style="background-color: #00aabb;">
                            <div class="talktext text-left">
                                <p>${output}</p>
                            </div>
                        </div>
                    </div>
                </div> 

                <a href="#" id="end">
                `;

                document.getElementById('input').value = '';
                msg.innerHTML = msgLines; // setando os as novas msgs
                window.location.href = '#end'; // rolar pro final da page
                document.getElementById('input').focus(); // focar o input de perguntas
            }
        }
    }

    http.send();
}
window.location.href = '#end'; // rolar pro final da page