package repository;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import models.FicheLanguage;

@Repository
public interface FicheLanguageRepository extends JpaRepository<FicheLanguage, Integer>{

}
