package controllers;

import java.util.List;
import models.FicheLanguage;
import repository.FicheLanguageRepository;
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
@RequestMapping("/api/fiche_language")
@CrossOrigin(origins = "*")
public class FicheLanguageController {

    
	@Autowired
	private FicheLanguageRepository ficheLanguageRepository;

    
	@GetMapping 
	public List<FicheLanguage> getAllFicheLanguages() {
	    return ficheLanguageRepository.findAll();
	}
	
	@GetMapping("/{id}")
	public ResponseEntity<FicheLanguage> getFicheLanguageById(@PathVariable Integer id) {
	    FicheLanguage ficheLanguage = ficheLanguageRepository.findById(id).orElseThrow(() -> new Exception("FicheLanguage avec l' id " + id + " n'existe pas"));
	    return ResponseEntity.ok(ficheLanguage);
	}
	
	@PostMapping 
	public FicheLanguage saveFicheLanguage(@RequestBody FicheLanguage newFicheLanguage) {
	    return ficheLanguageRepository.save(newFicheLanguage);
	}
	
	@PutMapping("/{id}") 
	public FicheLanguage updateFicheLanguage(@PathVariable Integer id, @RequestBody FicheLanguage updatedFicheLanguage) {
	    FicheLanguage ficheLanguage = ficheLanguageRepository.findById(id).orElseThrow(() -> new Exception("FicheLanguage avec l' id " + id + " n'existe pas"));
	    updateFicheLanguage.setIdFicheLanguage(id);
	    return udpateFicheLanguage.save(updatedFicheLanguage);
	}
	
	@DeleteMapping("/{id}") 
	public ResponseEntity<Map<String, Boolean>> deleteFicheLanguage(@PathVariable Integer id) {
	    FicheLanguage ficheLanguage = ficheLanguageRepository.findById(id).orElseThrow(() -> new Exception("FicheLanguage avec l' id " + id + " n'existe pas"));
	    ficheLanguageRepository.delete(ficheLanguage);
	    Map<String, Boolean> response = new HashMap<>();
	    response.put("deleted", Boolean.TRUE);
	    return ResponseEntity.ok(response);
	}
	
}