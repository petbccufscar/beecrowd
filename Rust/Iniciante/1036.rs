use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let mut tokens = buffer.split_whitespace();

	let a: f64 = tokens.next().unwrap().parse()?;
	let b: f64 = tokens.next().unwrap().parse()?;
	let c: f64 = tokens.next().unwrap().parse()?;

	let delta: f64 = b.powf(2.0) - 4.0 * a * c;

	if delta < 0.0 || a == 0.0 {
		println!("Impossivel calcular");
	} else {
		let r1: f64 = (-b + delta.sqrt()) / (2.0 * a);
		let r2: f64 = (-b - delta.sqrt()) / (2.0 * a);

		println!("R1 = {:.5}", r1);
		println!("R2 = {:.5}", r2);
	}

	Ok(())
}