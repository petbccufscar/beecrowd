use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let mut tokens = buffer.split_whitespace();

	let x: f64 = tokens.next().unwrap().parse()?;
	let y: f64 = tokens.next().unwrap().parse()?;

	if x == 0.0 && y == 0.0 {
		println!("Origem");
	} else if x == 0.0 {
		println!("Eixo Y");
	} else if y == 0.0 {
		println!("Eixo X");
	} else {
		if x > 0.0 {
			if y > 0.0 {
				println!("Q1");
			} else {
				println!("Q4");
			}
		} else {
			if y > 0.0 {
				println!("Q2");
			} else {
				println!("Q3");
			}
		}
	}

	Ok(())
}