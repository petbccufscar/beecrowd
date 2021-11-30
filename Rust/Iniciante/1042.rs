use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let tokens = buffer.split_whitespace();

	let original_numbers: Vec<i64> = tokens.map(|v| v.parse().unwrap()).collect();

	let mut sorted_numbers = original_numbers.clone();
	sorted_numbers.sort();

	for n in sorted_numbers {
		println!("{}", n);
	}

	println!("");

	for n in original_numbers {
		println!("{}", n);
	}

	Ok(())
}