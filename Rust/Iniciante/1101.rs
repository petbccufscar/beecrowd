use std::io;
use std::error::Error;
use std::cmp::max;
use std::cmp::min;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	loop {
		buffer.clear();
		stdin.read_line(&mut buffer)?;
		let mut tokens = buffer.split_whitespace();

		let m: i64 = tokens.next().unwrap().parse()?;
		let n: i64 = tokens.next().unwrap().parse()?;

		if m <= 0 || n <= 0 {
			break;
		}

		let s: i64 = min(m, n);
		let e: i64 = max(m, n);

		let mut soma: i64 = 0;

		for i in s..e+1 {
			soma += i;
			print!("{} ", i);
		}

		println!("Sum={}", soma);
	}

	Ok(())
}