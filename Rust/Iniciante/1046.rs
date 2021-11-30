use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let mut tokens = buffer.split_whitespace();

	let inicio: i64 = tokens.next().unwrap().parse()?;
	let fim: i64 = tokens.next().unwrap().parse()?;

	let duracao: i64;

	if inicio == fim {
		duracao = 24;
	} else if inicio > fim {
		duracao = 24 - inicio + fim;
	} else {
		duracao = fim - inicio;
	}

	println!("O JOGO DUROU {} HORA(S)", duracao);

	Ok(())
}