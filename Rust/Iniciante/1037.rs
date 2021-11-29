use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let valor: f64 = buffer.trim().parse()?;

	if valor > 100.0 {
		println!("Fora de intervalo");
	} else if valor > 75.0 {
		println!("Intervalo (75,100]");
	} else if valor > 50.0 {
		println!("Intervalo (50,75]");
	} else if valor > 25.0 {
		println!("Intervalo (25,50]");
	} else if valor >= 0.0 {
		println!("Intervalo [0,25]");
	} else {
		println!("Fora de intervalo");
	}

	Ok(())
}