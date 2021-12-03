use std::io;
use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	stdin.read_line(&mut buffer)?;

	let n: i64 = buffer.trim().parse()?;

	for _ in 0..n {
		buffer.clear();
		stdin.read_line(&mut buffer)?;

		let m: i64 = buffer.trim().parse()?;

		if m == 0 {
			println!("NULL");
		} else if m % 2 == 0 {
			if m > 0 {
				println!("EVEN POSITIVE");
			} else {
				println!("EVEN NEGATIVE");
			}
		} else {
			if m > 0 {
				println!("ODD POSITIVE");
			} else {
				println!("ODD NEGATIVE");
			}
		}
	}

	Ok(())
}