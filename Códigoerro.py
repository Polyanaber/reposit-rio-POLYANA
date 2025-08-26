function mensagem() {
    const usuarios = [
        {login: "Laura", senha: "1234"},
        {login: "Carlos", senha: "abcd"},
        {login: "Mariana", senha: "5678"}
    ];

    const loginDigitado = document.getElementById("Login").value;
    const senhaDigitada = document.getElementById("senha").value;
    const mensagem = document.getElementById("mensagem");
    let encontrado = false;

    for (let i = 0; i < usuarios.length; i++) {
        if (loginDigitado === usuarios[i].login && senhaDigitada === usuarios[i].senha) {
            encontrado = true;
            mensagem.innerHTML = "Bem-vindo, " + usuarios[i].login + "!";
            break; // encerra o loop depois que encontrar
        }
    }

    if (!encontrado) {
        mensagem.innerHTML = "Login ou senha incorretos";
    }
}
