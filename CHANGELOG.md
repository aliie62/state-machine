
# Change Log
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).
 

 
## [1.0.0] - 2022-04-08
First release with the **TCP Server** implementation . Details can be found [TCP CHANGELOG](tcp/CHANGELOG.md)

## [1.1.0] - 22-04-12

### Changed
- The project folder structure to accomodate the unit test files.
- randomisation utility function to accept arbitary exclusion list.
- The state machine randomisation approach so it will only be populated once in the beginning of the session.
- a control to make sure that at least one node has a edge to node "Z".

<br/>

### Added
- test folder and some test casses. However, it's not a completed list of all possible tests.
- Keyboard interruption signal handling to the client code.
- Added some printed guideline for the user.

<br/>

### Fixed
- Invalid data in the state machine transitions (edges) when the user put incorrect input (not "1", "2", or "3").
- table_fill method so that no nodes will have two same edges.

