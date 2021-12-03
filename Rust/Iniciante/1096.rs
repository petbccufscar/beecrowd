use std::error::Error;

fn main() -> Result<(), Box<dyn Error>> {
	
	for i in 0..5 {
		for j in 0..3 {
			println!("I={} J={}", 1 + i * 2, 7 - j);
		}
	}

	Ok(())
}