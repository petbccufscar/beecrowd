use std::io;
use std::error::Error;
use std::collections::HashMap;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;

	let mut tabela = HashMap::new();
	tabela.insert(61, "Brasilia");
	tabela.insert(71, "Salvador");
	tabela.insert(11, "Sao Paulo");
	tabela.insert(21, "Rio de Janeiro");
	tabela.insert(32, "Juiz de Fora");
	tabela.insert(19, "Campinas");
	tabela.insert(27, "Vitoria");
	tabela.insert(31, "Belo Horizonte");

	let ddd: i64 = buffer.trim().parse()?;

	if tabela.contains_key(&ddd) {
		println!("{}", tabela.get(&ddd).unwrap());
	} else {
		println!("DDD nao cadastrado");
	}

	Ok(())
}