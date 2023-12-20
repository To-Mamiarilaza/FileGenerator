package controllers;

import java.util.List;
import models.Fiche;
import repository.FicheRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


@RestController
@RequestMapping("/api/fiche")
@CrossOrigin(origins = "*")
public class FicheController {

    
	@Autowired
	private FicheRepository ficheRepository;

    
	@GetMapping 
	public List<Fiche> getAllFiches() {
	    return ficheRepository.findAll();
	}
	
	@GetMapping("/{id}")
	public ResponseEntity<Fiche> getFicheById(@PathVariable Integer id) {
	    Fiche fiche = ficheRepository.findById(id).orElseThrow(() -> new Exception("Fiche avec l' id " + id + " n'existe pas"));
	    return ResponseEntity.ok(fiche);
	}
	
	@PostMapping 
	public Fiche saveFiche(@RequestBody Fiche newFiche) {
	    return ficheRepository.save(newFiche);
	}
	
	@PutMapping("/{id}") 
	public Fiche updateFiche(@PathVariable Integer id, @RequestBody Fiche updatedFiche) {
	    Fiche fiche = ficheRepository.findById(id).orElseThrow(() -> new Exception("Fiche avec l' id " + id + " n'existe pas"));
	    updateFiche.setIdFiche(id);
	    return udpateFiche.save(updatedFiche);
	}
	
	@DeleteMapping("/{id}") 
	public ResponseEntity<Map<String, Boolean>> deleteFiche(@PathVariable Integer id) {
	    Fiche fiche = ficheRepository.findById(id).orElseThrow(() -> new Exception("Fiche avec l' id " + id + " n'existe pas"));
	    ficheRepository.delete(fiche);
	    Map<String, Boolean> response = new HashMap<>();
	    response.put("deleted", Boolean.TRUE);
	    return ResponseEntity.ok(response);
	}
	
}