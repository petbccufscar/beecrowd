use std::io;
use std::error::Error;
use std::collections::HashMap;

fn main() -> Result<(), Box<dyn Error>> {
	let stdin = io::stdin();
	let mut buffer = String::new();

	let mut meses = HashMap::new();
	meses.insert(1, "January");
	meses.insert(2, "February");
	meses.insert(3, "March");
	meses.insert(4, "April");
	meses.insert(5, "May");
	meses.insert(6, "June");
	meses.insert(7, "July");
	meses.insert(8, "August");
	meses.insert(9, "September");
	meses.insert(10, "October");
	meses.insert(11, "November");
	meses.insert(12, "December");

	stdin.read_line(&mut buffer)?;

	let mes: i64 = buffer.trim().parse()?;

	println!("{}", meses.get(&mes).unwrap());

	Ok(())
}