use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;

	let salario: f64 = buffer.trim().parse()?;

	let novo_salario: f64;
	let reajuste: f64;
	let percentual: f64;

	if salario > 2000.0 {
		percentual = 0.04;
	} else if salario > 1200.0 {
		percentual = 0.07;
	} else if salario > 800.0 {
		percentual = 0.10;
	} else if salario > 400.0 {
		percentual = 0.12;
	} else {
		percentual = 0.15;
	}

	reajuste = percentual * salario;
	novo_salario = salario + reajuste;

	println!("Novo salario: {:.2}", novo_salario);
	println!("Reajuste ganho: {:.2}", reajuste);
	println!("Em percentual: {} %", (percentual * 100.0) as i64);

	Ok(())
}