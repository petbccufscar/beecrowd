use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;

	let salario: f64 = buffer.trim().parse()?;
	let mut imposto: f64 = 0.0;

	if salario > 4500.0 {
		imposto += (salario - 4500.0) * 0.28;
		imposto += 1500.0 * 0.18;
		imposto += 1000.0 * 0.08;
	} else if salario > 3000.0 {
		imposto += (salario - 3000.0) * 0.18;
		imposto += 1000.0 * 0.08;
	} else if salario > 2000.0 {
		imposto += (salario - 2000.0) * 0.08;
	}

	if imposto > 0.0 {
		println!("R$ {:.2}", imposto);
	} else {
		println!("Isento");
	}

	Ok(())
}