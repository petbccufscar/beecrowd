use std::io;
use std::error::Error;
use std::cmp::max;
use std::cmp::min;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;
	
	let n: i64 = buffer.trim().parse()?;

	for _ in 0..n {
		buffer.clear();
		stdin.read_line(&mut buffer)?;
		let mut tokens = buffer.split_whitespace();

		let x: i64 = tokens.next().unwrap().parse()?;
		let y: i64 = tokens.next().unwrap().parse()?;

		let mut soma: i64 = 0;

		for j in (min(x, y)+1)..max(x, y) {
			if j % 2 == 1 {
				soma += j;
			}
		}

		println!("{}", soma);
	}

	Ok(())
}