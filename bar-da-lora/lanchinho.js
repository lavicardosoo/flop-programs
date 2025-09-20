import express from 'express';
import mysql from 'mysql2';
import cors from 'cors';

const levaETraz = express();

levaETraz.use(cors());

const conexao = mysql.createConnection({
    host: "localhost",
    user: "kittycat",
    password: "carpaccio",
    database: "BarDaLora"
});

levaETraz.get("/cardapio",(req,res) => {
    conexao.query("SELECT * FROM cardapio",(erro, result)=>{
        res.json(result);
    });
});

levaETraz.listen(3000, () =>{
    console.log("\nACESSE POR AQUI MOR: http://localhost:3000/cardapio");
    conexao.query("SELECT * FROM cardapio",(erro, result)=>{
        console.log(result);
    });
});