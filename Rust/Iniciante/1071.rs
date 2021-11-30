use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	let mut x: i64 = buffer.trim().parse()?;

	buffer.clear();
	stdin.read_line(&mut buffer)?;
	let mut y: i64 = buffer.trim().parse()?;

	if x > y {
		let a = y;
		y = x;
		x = a;
	}

	let mut soma = 0;

	x += 1;

	for i in x..y {
		if (i % 2).abs() == 1 {
			soma += i;
		}
	}

	println!("{}", soma);

	Ok(())
}